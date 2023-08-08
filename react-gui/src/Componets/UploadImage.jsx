import { useEffect, useState } from "react";







const UploadImage = () => {
    const [imageName, setImageName] = useState([]);
    const [images, setImages] = useState([]);
    const [imageURLs, setImageURLs] = useState([]);

    const [isVisible, setIsVisible] = useState(true);
    
    useEffect(() => {
        if (images.length < 1) return;
        const newImageUrls = [];
        images.forEach(image => newImageUrls.push(URL.createObjectURL(image)));
        setImageURLs(newImageUrls);
    }, [images]);

    function onImageChange(e){
        count = 0;
        setImageName([e.target.files[0].name]);
        setImages([...e.target.files]);
    }

    let count = 0;
    return (
        <div>
            <input type="file" multiple accept="image/*" onChange={onImageChange} />
            { imageURLs.map(function(imageSrc, id){
                return(
                <div className="flex">
                    <img className="imagePreview" src={imageSrc} alt="" />
                    <div className="imageNameClass">{imageName[count]}</div>
                    <div>{id}</div>
                    <div className="removeImageClass"><span>X</span></div>
            </div>
                );
            } 
            
                )}
        </div>
    )
}

export default UploadImage; 