<template>
    <nav class="navbar navbar-expand navbar-light fixed-top">
        <div class="container">
            <div v-if="user" class="collapse navbar-collapse  d-flex justify-content-between">
                <div class="mr-auto justify-content-start">
                    <router-link to="/" class="navbar-brand">Home</router-link>
                </div>
                <ul class="navbar-nav mx-auto d-flex justify-content-center">
                    <li class="nav-item">
                        <router-link to="/clients" class="nav-link">Clients</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/sectors" class="nav-link">Sectors</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/projects" class="nav-link">Projects</router-link>
                    </li>
                </ul>
                <ul class="navbar-nav ml-auto justify-content-end">
                    <li class="nav-item">
                        <p class="nav-link">{{user.name}}</p>
                    </li>
                    <li class="nav-item">
                        <a href="javascript:void(0)" @click="handleLogout" class="btn btn-dark">Log out</a>
                    </li> 
                </ul>
            </div>
            <div v-else class="collapse navbar-collapse  d-flex justify-content-between">
                <div class="mr-auto justify-content-start">
                    <router-link to="/" class="navbar-brand">Home</router-link>
                </div>
                <ul class="navbar-nav ml-auto justify-content-end">
                    <li class="nav-item">
                        <router-link to="/login" class="po2 btn btn-outline-secondary">Login</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/register" class="btn btn-outline-secondary">Sign Up</router-link>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
import  { mapGetters } from 'vuex'

export default {
    name: 'NavBar',
    methods: {
        async handleLogout() {
            try {
                localStorage.removeItem('token');
                
                this.$store.dispatch('clearUser', null);
                this.$router.push('/login');
                console.log('Logged out successfully');
            } catch (error) {
                console.error('Error logging out:', error);
            }
        }
    },
    computed: {
        ...mapGetters(['user'])
    }
}
</script>

<style scoped>
.po2 {
  margin-right: 8px;
}
</style>