export interface Message {
    id: string;
    sessionId: string;
    sender: 'user' | 'bot' | 'system';
    content: string;
    timestamp: Date;
};

export interface sendMessageRequest {
    message: string;
    image_url?: string;
    sessionId: string;
}

export interface sendMessageResponse {
    query: string;
    answer: string;
    token_usage: {
        completion_tokens: number;
        prompt_tokens: number;
        total_tokens: number;
    },
    total_price: number;
    response_time: string;
    tools_used: string[];
}