import { useState } from "react";
import UploadImage from "../UploadImage";



const InstagramBotOptions = () => {
    const [postType, setPostType] = useState(""); // State for post type selection
    const [aspectRatio, setAspectRatio] = useState(""); // State for aspect ratio selection
    const [images, setImages] = useState([]);



    function handlePostTypeChange(type) {
        setPostType(type);
    }

    function handleAspectRatioChange(ratio) {
        setAspectRatio(ratio);
    }

    function addImages(img, imgURL){
        console.log(img);
        console.log(imgURL);
   
        const Options = {
            "Options" : {
                "type": postType,
                "ratio": aspectRatio,
                "images": img,
                "imageURL":imgURL
            }
        }
       
    }

    return(
        <div className="options">
            <div className="optionsForm">
                <div className="flex center Question"><span>What format do you want</span></div>
                <div id="typeOfPost" className="flex center answerOptions">
                    <div className="choice flex center">
                        <span>Single Picture Post</span>
                        <label className="switch">
                            <input
                                id="SinglePicture"
                                type="checkbox"
                                checked={postType === "SinglePicture"}
                                onChange={() => handlePostTypeChange("SinglePicture")}
                            />
                            <span className="slider round"></span>
                        </label>
                    </div>
                    <div className="choice flex center">
                        <span>Reel or Video</span>
                        <label className="switch">
                            <input
                                    id="Video"
                                    type="checkbox"
                                    checked={postType === "Video"}
                                    onChange={() => handlePostTypeChange("Video")}
                                />
                            <span className="slider round"></span>
                        </label>
                    </div>
                    <div className="choice flex center">
                        <span>Carousel</span>
                        <label className="switch">
                            <input
                                    id="Carousel"
                                    type="checkbox"
                                    checked={postType === "Carousel"}
                                    onChange={() => handlePostTypeChange("Carousel")}
                                />
                            <span className="slider round"></span>
                        </label>
                    </div>
                </div>





                <div  className="flex center Question"><span>What aspect ratio do you want?</span></div>
                <div id="pictureRatio" className="flex center answerOptions">
                    <div className="choice flex center">
                        <span>Original Sizing</span>
                        <label className="switch">
                            <input
                                    id="OriginalSizing"
                                    type="checkbox"
                                    checked={aspectRatio === "OriginalSizing"}
                                    onChange={() => handleAspectRatioChange("OriginalSizing")}
                                />
                            <span className="slider round"></span>
                        </label>
                    </div>
                    <div className="choice flex center">
                        <span>1:1</span>
                        <label className="switch">
                            <input
                                    id="1:1"
                                    type="checkbox"
                                    checked={aspectRatio === "1:1"}
                                    onChange={() => handleAspectRatioChange("1:1")}
                                />
                            <span className="slider round"></span>
                        </label>
                    </div>
                    <div className="choice flex center">
                        <span>4:5</span>
                        <label className="switch">
                            <input
                                    id="4:5"
                                    type="checkbox"
                                    checked={aspectRatio === "4:5"}
                                    onChange={() => handleAspectRatioChange("4:5")}
                                />
                            <span className="slider round"></span>
                        </label>
                    </div>
                    <div className="choice flex center">
                        <span>16:9</span>
                        <label className="switch">
                            <input
                                    id="16:9"
                                    type="checkbox"
                                    checked={aspectRatio === "16:9"}
                                    onChange={() => handleAspectRatioChange("16:9")}
                                />
                            <span className="slider round"></span>
                        </label>
                    </div>
                </div>
                <div className="flex center Question"><span>Choose your Media</span></div>
                <div>
                    <UploadImage  passImages={addImages}/>
                </div>
            </div>
        </div>
    )
}

export default InstagramBotOptions;