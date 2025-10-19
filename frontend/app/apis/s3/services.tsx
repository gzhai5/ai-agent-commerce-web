import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";


const s3 = new S3Client({
  region: process.env.NEXT_PUBLIC_AWS_REGION!,
  credentials: {
    accessKeyId: process.env.NEXT_PUBLIC_AWS_ACCESS_KEY_ID!,
    secretAccessKey: process.env.NEXT_PUBLIC_AWS_SECRET_ACCESS_KEY!
  }
});

export const uploadImageToS3 = async (file: File, key: string) => {
    const bucketName = process.env.NEXT_PUBLIC_AWS_S3_BUCKET!;
    const region = process.env.NEXT_PUBLIC_AWS_REGION!;

    // Convert to PNG
    const imageBitmap = await createImageBitmap(file);
    const canvas = document.createElement('canvas');
    canvas.width = imageBitmap.width;
    canvas.height = imageBitmap.height;
    const ctx = canvas.getContext('2d')!;
    ctx.drawImage(imageBitmap, 0, 0);

    // Re-encode as PNG blob
    const blob = await new Promise<Blob>((resolve, reject) => {
        canvas.toBlob((blob) => {
            if (blob) {
                resolve(blob);
            } else {
                reject(new Error('Failed to convert canvas to blob.'));
            }
        }, 'image/png');
    });
    const arrayBuffer = await blob.arrayBuffer();
    const bytes = new Uint8Array(arrayBuffer);

    const newFileKey = key.endsWith('.png') ? key : `${key}.png`;
    const putCommand = new PutObjectCommand({
        Bucket: bucketName,
        Key: newFileKey,
        Body: bytes,
        ContentType: 'image/png',
    });

    await s3.send(putCommand);
    return `https://${bucketName}.s3.${region}.amazonaws.com/${key.endsWith('.png') ? key : `${key}.png`}`;
};