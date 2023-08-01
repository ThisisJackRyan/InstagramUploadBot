import { useState } from "react";
import instaHomePageIMG from "../Assets/Phones.png";

import InstagramBotOptions from "./InstagramBotOptions";

const MainPage = () => {
    const [hide, setHide] = useState(false);

    const changeHide = () => {
        setHide((current) => !current);
    }
    return (
        <div >
            <div className="flex instagramBackground">
                <div className="Content">
                    <img src={instaHomePageIMG} alt="" />
                </div>
                <div className="QuickDescription">
                    <h1>Simplify Your Posting Process!</h1>
                    <p>
                    Are you tired of the time-consuming process of manually uploading photos to your Instagram account? 
                    Look no further! 
                    Take your Instagram game to the next level with our powerful Instagram Uploader Bot. 
                    </p>
                    <div className="btn">
                        <button onClick={changeHide}>Run Bot</button>
                    </div>
                </div>
            </div>
            <div>
                {hide ? <InstagramBotOptions />: <div>{hide}</div>}
            </div>
        </div>
    )
}

export default MainPage;