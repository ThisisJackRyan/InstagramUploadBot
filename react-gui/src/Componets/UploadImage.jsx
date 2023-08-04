import { useEffect, useState } from "react";







const UploadImage = () => {

    const [images, setImages] = useState([]);
    const [imageURLs, setImageURLs] = useState([]);
    
    useEffect(() => {
        if (images.length < 1) return;
        const newImageUrls = [];
        images.forEach(image => newImageUrls.push(URL.createObjectURL(image)));
        setImageURLs(newImageUrls);
    }, [images]);

    const onImageChange = (e) => {
        console.log("images: " + images);
        console.log("imageURLs: " +imageURLs)
        setImages([...e.target.files]);
    }

    return (
        <div>
            <input type="file" multiple accept="image/*" onChange={onImageChange} />
            { imageURLs.map(imageSrc => <img src={imageSrc} />)}
        </div>
    )
}

export default UploadImage; 