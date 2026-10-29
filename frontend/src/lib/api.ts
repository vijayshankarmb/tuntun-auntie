
const API_URL = process.env.NEXT_PUBLIC_API_URL

export const apiFetch = async (
    endpoint: string,
    options: RequestInit = {}
) => {
    if (!API_URL) {
        throw new Error("NEXT_PUBLIC_API_URL is not configured")
    }

    return fetch(`${API_URL}${endpoint}`, {
        ...options,
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            ...options.headers
        }
    })
}