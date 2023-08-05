import { useEffect, useState } from "react";







const UploadImage = () => {
    const [imageName, setImageName] = useState([]);
    const [images, setImages] = useState([]);
    const [imageURLs, setImageURLs] = useState([]);
    
    useEffect(() => {
        if (images.length < 1) return;
        const newImageUrls = [];
        images.forEach(image => newImageUrls.push(URL.createObjectURL(image)));
        setImageURLs(newImageUrls);
    }, [images]);

    const onImageChange = (e) => {
        /*
        var files = event.target.files;
        var fileName = files[0].name;*/
        count = 0;
        console.log(e.target.files[0].name);
        setImageName([e.target.files[0].name])
        setImages([...e.target.files]);
    }
    let count = 0;
    return (
        <div>
            <input type="file" multiple accept="image/*" onChange={onImageChange} />
            { imageURLs.map(imageSrc  => 
            <div className="flex">
                <img className="imagePreview" src={imageSrc} />
                <div className="removeImageClass">{imageName[count++]}</div>
            </div>
                )}
        </div>
    )
}

export default UploadImage; 