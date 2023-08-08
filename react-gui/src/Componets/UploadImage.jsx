import { useEffect, useState } from "react";







const UploadImage = () => {
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
        setImages([...e.target.files]);
    }
    function ShortenString(ImageName){
        let maxLength = 20;
        console.log(ImageName.length);
        if(ImageName.length <= maxLength+3){
            return ImageName;
        }
        
        let NewName = ImageName.substring(0,maxLength-3) + "...";
        let type = ImageName.substring(ImageName.length-3,ImageName.length);
        return NewName + type;      
    }

    return (
        <div>
            <input type="file" multiple accept="image/*" onChange={onImageChange} />
            { imageURLs.map(function(imageSrc, index){
                return(
                <div className="flex">
                    {console.log()}
                    <img className="imagePreview" src={imageSrc} alt="" />
                    <div className="imageNameClass">{ShortenString(images[index].name)}</div>
                    <div className="removeImageClass"><span>X</span></div>
                </div>);
                } )}
        </div>
    )
}

export default UploadImage; 