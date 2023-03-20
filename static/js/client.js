let camera_button = document.querySelector("#start-camera");
let video = document.querySelector("#video");
let start_button = document.querySelector("#start-record");
let stop_button = document.querySelector("#stop-record");
let download_link = document.querySelector("#download-video");
let file_input = document.querySelector("#id_video");
let show_classification = document.querySelector("#classification");


let camera_stream = null;
let media_recorder = null;
let blobs_recorded = [];

let upload_button = document.querySelector("#Upload");

camera_button.addEventListener('click', async function() {
   	try {
    	camera_stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
    }
    catch(error) {
    	alert(error.message);
    	return;
    }

    video.srcObject = camera_stream;
    camera_button.style.display = 'none';
    video.style.display = 'block';
    start_button.style.display = 'block';
});

start_button.addEventListener('click', function() {
    media_recorder = new MediaRecorder(camera_stream, { mimeType: 'video/webm' });

    media_recorder.addEventListener('dataavailable', function(e) {
    	blobs_recorded.push(e.data);
    });

    media_recorder.addEventListener('stop',
        function () {
            let video_local = URL.createObjectURL(new Blob(blobs_recorded, {type: 'video/webm'}));
            download_link.href = video_local;

            let recording = new File(blobs_recorded, 'recording.webm', {type: 'video/webm'});

            const dataTransfer = new DataTransfer();
            dataTransfer.items.add(recording);
            file_input.files = dataTransfer.files;


            var form = new FormData();
            form.append('video', recording);


             $.ajax({
                type: "POST",
                url: 'classification',
                data : form,
                cache: false,
                contentType: false,
                processData: false,
                success: classification
            });

            function classification(response) {
                document.getElementById("classification").innerHTML = response.classification;
            }




            stop_button.style.display = 'none';
            download_link.style.display = 'block';

        });

    media_recorder.start(1000);

    start_button.style.display = 'none';
    stop_button.style.display = 'block';
});

stop_button.addEventListener('click', function() {
	media_recorder.stop();
});




