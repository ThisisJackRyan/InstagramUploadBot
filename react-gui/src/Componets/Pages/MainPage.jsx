import instaHomePageIMG from "../Assets/Phones.png"



const MainPage = () => {
    return (
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
                    <button>Run Bot</button>
                </div>
            </div>
        </div>
    )
}

export default MainPage;