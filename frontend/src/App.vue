<template>
  <div id="app" style="padding-top: 90px;">
  <NavBar />
  
  <router-view />
  </div>

</template>

<script>
import axios from 'axios';
import NavBar from './components/NavBar.vue';

export default {
  name: 'App',
  components: {
    NavBar
  },

  async created() {
  if (!this.$store.state.user) {
    await this.fetchUser();
    }
  },

  methods: {
    async fetchUser() {
      try {
        const token = localStorage.getItem('token');
        if (!token) {
          console.log('No token found');
          return;
        }

        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        const response = await axios.get('user');
        if (response && response.data) {
          this.$store.dispatch('setUser', response.data);
          console.log('User data response:', response.data);
        } else {
          console.error('Invalid user data response:', response);
        }
      } catch (error) {
        console.error('Error fetching user:', error);
      }
    },
    handleLogout() {
      this.$store.dispatch('clearUser');
      localStorage.removeItem('token');
      this.$router.push('/login');
    }
  },
  beforeRouteEnter(to, from, next) {
    next(vm => {
      vm.fetchUser();
    });
  }
};
</script>

<style>
* {
    box-sizing: border-box
}

body, html, #app, #root, .auth-wrapper {
  width: 100%;
  height: 100%;
  
}
.navbar-light {
  background-color: #ffffff;
  box-shadow: 0px 14px 80px rgba(34, 35,58, 0.2);
}
</style>