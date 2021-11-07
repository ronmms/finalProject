import './App.css';
import { useState, useRef } from 'react';
import service from './api';
import './App.css';

function App() {
    const stringRef = useRef();
    const [md5, setMd5] = useState(null);

    const generateNewMd5OnClick = () => {
        const md5string = stringRef.current.value;
        service.setMd5(md5string).then(res=>setMd5(res.md5str));
    };

    return (
        <div className={'app'}>
            <div>
                enter a string to encrypt:
                <input type='string' ref={stringRef} />
                <button onClick={generateNewMd5OnClick}>set md5</button>
                <br/>
                {md5}
            </div>
        </div>
    );
}

export default App;