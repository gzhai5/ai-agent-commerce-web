import { mcpInstance } from '../base/mcp.instance';
import { sendMessageRequest, sendMessageResponse } from './interfaces';


export const sendMessage = async (body: sendMessageRequest): Promise<sendMessageResponse> => {
    const response = await mcpInstance.post('/query', body);
    return response.data as sendMessageResponse;
};