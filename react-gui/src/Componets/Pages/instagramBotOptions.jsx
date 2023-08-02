
//first chuck is multiple choice 
//Second chunk 

const InstagramBotOptions = () => {
    return(
        <div className="options">
            <div className="optionsForm">
                <div className="flex center Question"><span>What format do you want</span></div>
                <div id="typeOfPost" className="flex center answerOptions">
                    <div className="choice flex center">
                        <span>Single Picture Post</span>
                        <label className="switch">
                            <input id="SinglePicture" type="checkbox" />
                            <span className="slider round"></span>
                        </label>
                    </div>
                    <div className="choice flex center">
                        <span>Reel or Video</span>
                        <label className="switch">
                            <input id="SinglePicture" type="checkbox" />
                            <span className="slider round"></span>
                        </label>
                    </div>
                    <div className="choice flex center">
                        <span>Carousel</span>
                        <label className="switch">
                            <input id="SinglePicture" type="checkbox" />
                            <span className="slider round"></span>
                        </label>
                    </div>
                </div>
                <div  className="flex center Question"><span>What aspect ratio do you want?</span></div>
                <div id="pictureRatio" className="flex center answerOptions">
                    <div className="choice flex center">
                        <span>Original Sizing</span>
                        <label className="switch">
                            <input id="SinglePicture" type="checkbox" />
                            <span className="slider round"></span>
                        </label>
                    </div>
                    <div className="choice flex center">
                        <span>1:1</span>
                        <label className="switch">
                            <input id="SinglePicture" type="checkbox" />
                            <span className="slider round"></span>
                        </label>
                    </div>
                    <div className="choice flex center">
                        <span>4:5</span>
                        <label className="switch">
                            <input id="SinglePicture" type="checkbox" />
                            <span className="slider round"></span>
                        </label>
                    </div>
                    <div className="choice flex center">
                        <span>16:9</span>
                        <label className="switch">
                            <input id="SinglePicture" type="checkbox" />
                            <span className="slider round"></span>
                        </label>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default InstagramBotOptions;