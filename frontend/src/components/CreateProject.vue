<template>
<div class="app">
  <div class="auth-inner">
    <h1>Add New Project</h1>
    
    <!-- Create Project Form -->
    <form @submit.prevent="createProject">
      <label>Project Name:</label>
      <input type="text" class="form-control" v-model="newProject.project_name" required>
      <label>Details:</label>
      <textarea class="form-control" v-model="newProject.details" required></textarea>
      <label class="form-group">Client:</label>
      <select class="form-control" v-model="newProject.client_name" required>
        <option value="">Select a client</option>
        <option v-for="client in clients" :key="client.id" :value="client.id">{{ client.name }}</option>
      </select>
      <label class="form-group">Sector:</label>
      <select class="form-control" v-model="newProject.sector" required>
        <option value="">Select a project sector</option>
        <option v-for="sector in sectors" :key="sector.id" :value="sector.id">{{ sector.sector }}</option>
      </select>
      <button type="submit" class="btn btn-outline-secondary">Add Project</button>
    </form>
    
    <!-- Error Message -->
    <p v-if="error" class="error-message">{{ error }}</p>
  </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CreateProject',

  data() {
    return {
      newProject: {
        project_name: '',
        details: '',
        client_name: '',
        sector: ''
      },
      clients: [],
      sectors: [],
      error: null
    };
  },

  async created() {
    try {
      await this.fetchClients();
      await this.fetchSectors();
    } catch (error) {
      console.error('Error in created hook:', error);
      this.error = 'Failed to fetch data. Please try again later.';
    }
  },

  methods: {
    async fetchClients() {
  try {
    const token = localStorage.getItem('token');
    if (!token) {
      throw new Error('No token found');
    }
    const response = await axios.get('clients/', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    this.clients = response.data;
    console.log('Clients:', this.clients);
  } catch (error) {
    console.error('Error fetching clients:', error);
    this.error = 'Failed to fetch clients. Please try again later.';
  }
},

    async fetchSectors() {
  try {
    const token = localStorage.getItem('token');
    if (!token) {
      throw new Error('No token found');
    }
    const response = await axios.get('sectors/', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    this.sectors = response.data;
    console.log('Sectors:', this.sectors);
  } catch (error) {
    console.error('Error fetching sectors:', error);
    this.error = 'Failed to fetch sectors. Please try again later.';
  }
},

    async createProject() {
      try {
        const token = localStorage.getItem('token');
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        await axios.post('projects/', this.newProject);
        this.$router.push('/projects');
      } catch (error) {
        console.error('Error creating project:', error);
        this.error = 'Failed to create project. Please try again.';
      }
    }
  }
};
</script>

<style scoped>
button {
  margin-top: 10px;
}
label {
  margin-top: 10px;
  margin-bottom: 4px;
}
input, select, textarea {
  width: 500px;
}

#app {
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
.auth-inner {
  width: 600px;
  margin: auto;
  background: #ffffff;
  box-shadow: 0px 14px 80px rgba(34, 35,58, 0.3);
  padding: 40px 55px 45px 55px;
  border-radius: 15px;
  transition: all .3s;
}
.auth-inner h1 {
  text-align: center;
  margin: 0;
  line-height: 1;
  padding-bottom: 20px
}
</style>