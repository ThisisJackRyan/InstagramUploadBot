
//first chuck is mutiple choice 
//Second chunk 

const InstagramBotOptions = () => {
    return(
        <div className="options">
            <div className="optionsForm">
                <div className="flex center Question"><span>What format do you want</span></div>
                <div id="typeOfPost" className="flex center">
                    <div className="choice flex center">
                        <span>Single Picture Post</span>
                        <label className="switch">
                            <input id="SinglePicture" type="checkbox" />
                            <span className="slider round"></span>
                        </label>
                    </div>
                    <div className="choice">
                        <span>Reel or Video</span>
                        <label className="switch">
                            <input id="SinglePicture" type="checkbox" />
                            <span className="slider round"></span>
                        </label>
                    </div>
                    <div className="choice">
                        <span>Carousel</span>
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