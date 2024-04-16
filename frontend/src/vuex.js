import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      user: null
    };
  },
  getters: {
    user(state) {
      return state.user;
    }
  },
  actions: {
    setUser(context, user) {
      context.commit('setUser', user);
    },
    clearUser(context) {
      context.commit('clearUser');
    }
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    clearUser(state) {
      state.user = null;
    }
  }
});

export default store;
