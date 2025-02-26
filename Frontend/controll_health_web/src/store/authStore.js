import { create } from "zustand";

const useAuthStore = create((set) => ({
  user: null,
  token: sessionStorage.getItem("access_token") || null,
  login: (token, userData) => {
    sessionStorage.setItem("access_token", token);
    set({ user: userData, token });
  },
  logout: () => {
    sessionStorage.removeItem("access_token");
    set({ user: null, token: null });
  },
}));

export default useAuthStore;
