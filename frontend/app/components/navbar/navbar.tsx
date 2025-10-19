import React from "react";
import { Ellipsis } from 'lucide-react';


export default function Navbar() {

    return (
        <div className="navbar bg-base-100 shadow-sm">
            <div className="flex-1">
                <a className="btn btn-ghost text-xl">Commerce Website XXX</a>
            </div>
            <div className="flex-none">
                <button className="btn btn-square btn-ghost">
                    <Ellipsis className="inline-block h-5 w-5 stroke-current" />
                </button>
            </div>
        </div>
    )
}