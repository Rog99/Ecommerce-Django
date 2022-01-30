'use strict';
function LikeButton(){
    const [messages, setMessages] = new React.useState([
        {type: 'sender', message: 'Hey Vishnu'},
        {type: 'receiver', message: 'Hi seller'},
        {type: 'sender', message: 'Can I get som more info on the product'},
        {type: 'receiver', message: 'Sure :-)'}
    ]);
    return (
    <div>
        {messages.map((text) => (
            <div class={text.type}>{text.message}</div>
        ))}
    </div>
    )
}

const domContainer = document.querySelector('#chat-log');
ReactDOM.render(<LikeButton/>, domContainer);