<template>
  <div class="app">
    <div class="auth-inner">
      <form @submit.prevent="handleSubmit">
        <h3>Login</h3>

        <div class="form-group">
          <label>Email</label>
          <input type="email" class="form-control" v-model="email" placeholder="Email" required />
        </div>
        <div class="form-group">
          <label>Password</label>
          <input type="password" v-model="password" class="form-control" placeholder="Password" required />
        </div>

        <button type="submit" class="btn btn-primary btn-block">Login</button>
      </form>

    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginPage',

  data() {
    return {
      email: '',
      password: ''
    }
  },

  methods: {
    async handleSubmit() {
      try {
        const response = await axios.post('login', {
          email: this.email,
          password: this.password
        });

        if (response && response.data && response.data.token) {
          localStorage.setItem('token', response.data.token);
          this.$store.dispatch('setUser', response.data.user);
          await this.$root.fetchUser();
          this.$router.push('/');
        } else {
          console.error('Invalid login response:', response);
        }
      } catch (error) {
        console.error('Error logging in:', error);
      }
    }
  }
}
</script>


<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Fira+sans:400,500,600,700,800');

  

  body {
    background: #1c8ef9 !important;
    min-height: 100vh;
    display: flex;
    font-weight: 400;
    font-family: 'Fira Sans', sans-serif;
  }

  h1, h2, h3, h4, h5, h6, label, span {
    font-weight: 500;
    font-family: 'Fira Sans', sans-serif;
  }

  body, html, #app, #root, .auth-wrapper {
    width: 100%;
    height: 100%
  }

  #app {
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

  .auth-inner {
    width: 470px;
    margin: auto;
    background: #ffffff;
    box-shadow: 0px 14px 80px rgba(34, 35,58, 0.4);
    padding: 40px 55px 45px 55px;
    border-radius: 15px;
    transition: all .3s;
  }

  .auth-inner h3 {
    text-align: center;
    margin: 0;
    line-height: 1;
    padding-bottom: 20px
  }

  .custom-control-label {
    font-weight: 400;
  }

  .forgot {
    padding-top: 10px;
    font-size: 0.9em;
  }
</style>