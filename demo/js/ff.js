(function () {
    //var newMp = new Mprogress('start');
    var mp1 = new Mprogress({
        parent: '#scratch'
    });
    var mp2 = new Mprogress({
        parent: '#up'
    });
    var mp3 = new Mprogress({
        parent: '#singelhand'
    });
    var mp4 = new Mprogress({
        parent: '#narrow'
    });
    var mp5 = new Mprogress({
        parent: '#ear'
    });
    var mp6 = new Mprogress({
        parent: '#down'
    });
    var mp7 = new Mprogress({
        parent: '#point'
    });
    var mp8 = new Mprogress({
        parent: '#raise'
    });
    var mp9 = new Mprogress({
        parent: '#thumb'
    });
    var mp10 = new Mprogress({
        parent: '#singelhandr'
    });
    var mp11 = new Mprogress({
        parent: '#round'
    });



    function bindEvent() {

        $("#demoDeStart").click(function () {
            mp1.start();
            mp2.start();
            mp3.start();
            mp4.start();
            mp5.start();
            mp6.start();
            mp7.start();
            mp8.start();
            mp9.start();
            mp10.start();
        });
        $("#demoDeSet").click(function () {
            mp1.set(0.4);
            mp2.set(0.4);
            mp3.set(0.4);
            mp4.set(0.4);
            mp5.set(0.4);
            mp6.set(0.4);
            mp7.set(0.4);
            mp8.set(0.4);
            mp9.set(0.4);
            mp10.set(0.4);
        });
        $("#demoDeInc").click(function () {
            mp1.inc();
            mp2.inc();
            mp3.inc();
            mp4.inc();
            mp5.inc();
            mp6.inc();
            mp7.inc();
            mp8.inc();
            mp9.inc();
            mp10.inc();
        });
        $("#demoDeEnd").click(function () {
            mp1.end(true);
            mp2.end(true);
            mp3.end(true);
            mp4.end(true);
            mp5.end(true);
            mp6.end(true);
            mp7.end(true);
            mp8.end(true);
            mp9.end(true);
            mp10.end(true);
        });


    }

    bindEvent();

    // const socket = new WebSocket('ws://0.0.0.0:8081');

    // // Connection opened
    // socket.addEventListener('open', function (event) {
    //     socket.send('Hello Server!');
    // });

    // // Listen for messages
    // socket.addEventListener('message', function (event) {
    //     console.log('Message from server ', event.data);
    // });
    var socket;
    if ("WebSocket" in window) {
        var ws = new WebSocket("ws://127.0.0.1:8081/test");
        socket = ws;
        ws.onopen = function () {
            console.log('连接成功');
            // alert("测试模式启动成功, 请刷新网页");
        };
        ws.onmessage = function (evt) {
            var received_msg = evt.data;
            String(received_msg)
            received_msg = received_msg.split("$")
            document.getElementById("showMes").value += received_msg + "\n";
            var n1 = Number(received_msg[1])
            var n2 = Number(received_msg[2])
            var n3 = Number(received_msg[3])
            var n4 = Number(received_msg[4])
            var n5 = Number(received_msg[5])
            var n6 = Number(received_msg[6])
            var n7 = Number(received_msg[7])
            var n8 = Number(received_msg[8])
            var n9 = Number(received_msg[9])
            var n10 = Number(received_msg[10])
            var n11 = Number(received_msg[11])
            mp1.set(n1);
            mp2.set(n2);
            mp3.set(n3);
            mp4.set(n4);
            mp5.set(n5);
            mp6.set(n6);
            mp7.set(n7);
            mp8.set(n8);
            mp9.set(n9);
            mp10.set(n10);
            mp11.set(n11);
        };
        ws.onclose = function () {
            alert("测试模式启动成功, 请刷新网页");
        };
    } else {
        alert("浏览器不支持WebSocket");
    }



    function sendMeg() {
        var message = document.getElementById("name").value + "$" + document.getElementById("mes").value;
      
        document.getElementById("showMes").value += message + "\n\n";

        
        socket.send(message);
    }
    function bindEvent() {

        $("#send").click(function () {
           sendMeg();
        });
    }
 

}())