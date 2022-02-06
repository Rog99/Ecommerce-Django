'use strict';

function ChatMessages({type, message}){
    return (
        <div className={type}>{message}</div>
    )
}

function ChatBox(){
    const [messages, setMessages] = React.useState([]);
    const [userId, setUserId] = React.useState(0);

    const textMessage = React.useRef(null);
    const buttonElement = React.useRef(null);

    const [chatSocket, setChatSocket] = React.useState(() => {
        let room_name = JSON.parse(document.getElementById('room-name').textContent);
        return new WebSocket(`ws://${window.location.host}/ws/chat/${room_name}/`);
    })

    React.useEffect(() => {
        console.log(userId, messages)
    }, [messages, userId])

    React.useEffect(() => {
        console.log('data')
        fetch('http://'+ window.location.host +'/get-user')
        .then(res => res.json())
        .then(data => setUserId(data.user_id))
        .catch(err => console.log(err))
    }, [userId])

    React.useEffect(() => {
        chatSocket.onmessage = function(e){
            let data = JSON.parse(e.data);
            setMessages((message) => [...message, data]);
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
            {messages.map(text => <ChatMessages message={text.message} type={userId==text.user_id ? 'receiver': 'sender'}/>)}
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