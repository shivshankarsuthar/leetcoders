import react,{useState} from 'react';

export default function Navbar(props){
    const [text,setText] = useState("Enter text here!");
    const handleTextChange = (event)=>{
        setText(event.target.value);
    };
    const handleButtonClick = (event)=>{
        setText(text.toUpperCase());
    }
    return (
        <>
        <input type="text" value={text} onChange={handleTextChange} />
        <button onClick={handleButtonClick}
        >Capitalise</button>
        <div>This is navbar {props.title}</div>
        </>
    );
}