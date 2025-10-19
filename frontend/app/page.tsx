/* eslint-disable @next/next/no-img-element */
import React from 'react';
import Navbar from './components/navbar/navbar';
import { ChatWidget } from './components/chat/chatWidget';
import logo from '../public/logo.png';


export default function Chat() {

    return (
        <div className='bg-base-100 min-h-screen'>
            <Navbar />

            <div className="min-h-screen bg-base-100 text-primary flex flex-col items-center">
                <img
                    src={logo.src}
                    alt="Commerce Website XXX Logo"
                    className="w-1/5 mt-6"
                />

                {/* Title Section */}
                <h1 className="text-5xl mt-4 font-bold text-black">Welcome to Commerce Website XXX</h1>
                <p className="text-xl mt-2 mb-6 font-semibold text-black">Ask us about our products! We have clothing, footwear, and handbags!</p>

                {/* Chat Widget spanning across page */}
                <div className="w-3/4 max-w-4xl">
                    <ChatWidget />
                </div>
            </div>
        </div>
    )
}