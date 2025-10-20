"use client";
import React, { useState, useRef, useEffect } from 'react';
import { Bot, Send as SendIcon, ImageUp, FolderCheck } from 'lucide-react';
import { Message } from '@/app/apis/chat/interfaces';
import { sendMessage } from '@/app/apis/chat/apis';
import { uploadImageToS3 } from '@/app/apis/s3/services';
import { generateUUID } from './utils';


export const ChatWidget = () => {
    const bottomRef = useRef<HTMLDivElement | null>(null);
    const [sessionId, setSessionId] = useState<string>('');
    const [query, setQuery] = useState<string>('');
    const [conversationHistory, setConversationHistory] = useState<Message[]>([]);
    const [selectedImage, setSelectedImage] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState<boolean>(false);


    // Ensure sessionId is set on component mount
    useEffect(() => {
        if (!sessionId) {
            setSessionId(generateUUID());
        }
    }, [sessionId]);


    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (query.trim() === '') return;

        // add the user input into the FE/BE, and reset the input box
        setIsLoading(true);
        const userMsgId = generateUUID();
        appendOneMessage(query, userMsgId, 'user');
        setQuery('');

        const s3ImageUrl = selectedImage ? await uploadImageToS3(
            await (await fetch(selectedImage)).blob() as File,
            `${generateUUID()}.jpg`
        ) : null;
        const combinedQuery = s3ImageUrl ? `Image URL: ${s3ImageUrl}\n ${query}` : query;
        const botResponse = await sendMessage({ message: combinedQuery, image_url: s3ImageUrl || "", sessionId });
        const botMessage: Message = {
            id: generateUUID(),
            sessionId,
            sender: 'bot',
            content: botResponse.answer,
            timestamp: new Date(),
        };
        appendOneMessage(botMessage.content, botMessage.id, 'bot');
        setIsLoading(false);
        setSelectedImage(null); // reset selected image after sending
    }

    // helper func to append one message to the conversation history
    const appendOneMessage = (message: string, msg_id: string, sender: string) => {
        setConversationHistory(prevHistory => [
            ...prevHistory,
            {
                id: msg_id,
                sessionId: sessionId,
                sender: sender,
                content: message,
                timestamp: new Date(),
            } as Message,
        ]);
    }

    const handleSelectingImage = (e: React.ChangeEvent<HTMLInputElement>) => {
        const file = e.target.files?.[0];
        if (!file) return;

        // 1️⃣ Check MIME type
        if (!file.type.startsWith("image/")) {
            alert("Please upload a valid image file (JPEG, PNG, etc.)");
            e.target.value = ""; // reset input
            return;
        }

        // 2️⃣ Check file size (optional, e.g. < 5MB)
        const maxSizeMB = 5;
        if (file.size > maxSizeMB * 1024 * 1024) {
            alert(`Image must be smaller than ${maxSizeMB}MB`);
            e.target.value = "";
            return;
        }

        // 3️⃣ Check if the image is actually readable
        const img = new Image();
        img.onload = () => {
            console.log("Image is valid and readable:", file);
            setSelectedImage(URL.createObjectURL(file));
        };
        img.onerror = () => {
            alert("The selected file is not a valid image or is corrupted.");
            e.target.value = "";
        };
        img.src = URL.createObjectURL(file);
    };

    // Scroll to the bottom of the chat when new messages are added or loading state changes
    useEffect(() => {
        if (bottomRef.current) {
            bottomRef.current.scrollIntoView({ behavior: 'smooth' });
        }
    }, [conversationHistory, isLoading]);


    return (
        <div className="flex flex-col h-full">
            <div className="flex-1 overflow-y-auto p-4">

                {/* Normal chat between user and bot */}
                <div className={`w-full h-5/6 min-h-[30rem] min-w-[25rem] min-h-[20rem] items-center justify-center rounded-lg z-10 bg-transport}`}>

                    {/* chat area */}
                    <div className='h-full w-full overflow-y-auto flex flex-col gap-4 px-2 relative'>
                        {conversationHistory.map((chat, index) => (
                            <div key={chat.id} className={`chat ${chat.sender !== 'user' ? 'chat-start' : 'chat-end'}`}>
                                
                                {/* avatar */}
                                <div className="chat-image avatar">
                                    <div className="w-10 h-10 rounded-full bg-zinc-100 flex text-[#5A3E00] items-center justify-center">
                                        {chat.sender === 'user' && <p className='text-2xl font-sans font-normal'>?</p>}
                                        {chat.sender !== 'user' && <Bot size={30} color="#5A3E00" />}
                                    </div>
                                </div>

                                {/* chat bubble */}
                                <div className={`chat-bubble max-w-[43rem] text-base font-semibold ${chat.sender === 'bot'? 'bg-[#EFE8D4] text-[#5A3E00] pb-8': 'bg-[#5A3E00] text-[#EFE8D4]'}`}>
                                    {chat.content}
                                </div>                                
                            </div>
                        ))}
                        {/* When user's query is pending, show the loading indicator */}
                        {isLoading && (
                            <div className="flex items-center justify-start pl-10">
                                <span className="loading loading-ring loading-xl text-purple-700"></span>
                                <span className="ml-2 text-lg text-purple-700">Thinking...</span>
                            </div>
                        )}
                    </div>

                    {/* chat input box */}
                    <form onSubmit={handleSubmit} className={`w-full bg-white h-[3.5rem] min-w-[25rem] mt-[5rem] p-2 flex flex-row items-center justify-center gap-2 rounded-md z-10 `}>
                        
                        {/* image upload button */}
                        <label htmlFor="image-upload" className="btn btn-ghost btn-square rounded-md hover:bg-[#E0D3B8] cursor-pointer">
                            <input
                                id="image-upload"
                                type="file"
                                accept="image/*"
                                className="hidden"
                                onChange={(e) => {handleSelectingImage(e) }}
                            />
                            {!selectedImage && <ImageUp className="text-black" />}
                            {selectedImage && <FolderCheck className="text-green-600" />}
                        </label>

                        <input 
                            type="text" 
                            placeholder="Ask about our products..." 
                            className="input bg-transparent w-full h-full text-lg text-[#5A3E00] placeholder-black font-semibold rounded-l-md px-3"
                            value={query}
                            onChange={(e) => setQuery(e.target.value)}
                            onKeyDown={(e) => {
                                if (e.key === 'Enter' && query.trim() !== '') {
                                    handleSubmit(e);
                                }
                            }}
                        />
                        <button type="submit" className="btn btn-ghost btn-square rounded-r-md hover:bg-[#E0D3B8]" disabled={query.trim() === ''}>
                            <SendIcon className="text-black" />
                        </button>
                    </form>

                    {/* Anchor to scroll to */}
                    <div ref={bottomRef} />
                </div>
            </div>
        </div>
    )
};