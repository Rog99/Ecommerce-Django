'use strict';

function ChatMessages({props}){
    return (
        <div className={props.type}>{props.message}</div>
    )
}

function ChatBox(){
    const [messages, setMessages] = React.useState([
        {type: 'sender', message: 'Hey Vishnu'},
        {type: 'receiver', message: 'Hi seller'},
        {type: 'sender', message: 'Can I get som more info on the product'},
        {type: 'receiver', message: 'Sure :-)'}
    ]);

    const textMessage = React.useRef(null);
    const buttonElement = React.useRef(null);

    const [chatSocket, setChatSocket] = React.useState(() => {
        let room_name = JSON.parse(document.getElementById('room-name').textContent);
        return new WebSocket(`ws://${window.location.host}/ws/chat/${room_name}/`);
    })

    React.useEffect(() => {
        chatSocket.onmessage = function(e){
            let data = JSON.parse(e.data);
            setMessages((message) => [...message, {type: 'receiver', message: data.message}]);
        }

        chatSocket.onclose = function(e){
            console.error('Chat socket closed unexpectedly');
        }
    }, [chatSocket])

    function sendMessage(){
        chatSocket.send(
            JSON.stringify({
                'message': textMessage.current.value
            })
        )
        textMessage.current.value = "";
    }

    function handleKey(e){
        if(e.keyCode == 13){
            buttonElement.current.click();
        }
    }


    return (
    <div>
        <div id="chat-log">
            {messages.map(text => <ChatMessages props={text}/>)}
        </div>
        <div id="input-elements">
            <input id="chat-message-input" type="text" ref={textMessage} onKeyUp={handleKey}/>
            <button id="chat-message-submit" onClick={sendMessage} ref={buttonElement}>Send</button>
        </div>
    </div>
    )
}

const domContainer = document.querySelector('#root');
ReactDOM.render(<ChatBox/>, domContainer);