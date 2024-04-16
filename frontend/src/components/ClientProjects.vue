<template>
  <!--If no Clients -->
  <div v-if="projects && projects.length === 0"><p>No projects available.</p>
    <router-link to="/new-project" taggert="_blank"><button class="btn btn-outline-secondary">CREATE PROJECT</button></router-link>
  </div>
  <!-- List of Projects -->
  <div v-else>
    <div v-if="projects && projects.length > 0">
      <h2>PROJECTS</h2>
      <ul class="list-group list-group-flush">
      <div class="list-group-item" v-for="project in projects" :key="project.client_name">
        <h4>Project name: <span>{{ project.project_name }}</span></h4>
        <h5 v-if="project.sector && sectors[project.sector]">Sector: <span>{{ sectors[project.sector] }}</span></h5>
        <br>
        <p>{{ project.details }}</p>
      </div>
      </ul>
    </div>
  </div>
  <!-- Error Message -->
  <p v-if="error" style="color: red;">{{ error }}</p>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ClientProjects',

  data() {
    return {
      projects: [],
      clients: {},
      sectors: {},
      error: null
    };
  },

  async created() {
    const client_pk = this.$route.params.id
    console.log('client_pk', client_pk)

    await this.fetchProjects(client_pk)
    await this.fetchClients()
    await this.fetchSectors()
  },

  methods: {
    //fetching projects using client id
    async fetchProjects(client_pk) {
      try {
        // retrieving user token
        const token = localStorage.getItem('token');
        const response = await axios.get(`clients/${client_pk}/projects/`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        this.projects = response.data;
        console.log('this.projects', this.projects)
      } 
      // errors
      catch (error) {
        console.error('Error fetching projects:', error);
        console.log('this.projects', this.projects) 
      }
    },

    //fetching errors
    async fetchClients() {
      try {
        //retrieving user token
        const token = localStorage.getItem('token');
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        const response = await axios.get('clients/');
        this.clients = response.data.reduce((map, client) => {
          map[client.id] = client.name;
          return map;
        }, {});
      }
      //errors
      catch (error) {
        console.error('Error fetching clients:', error);
      }
    },

    //fetching sectors
    async fetchSectors() {
      try {
        //retrieving user token
        const token = localStorage.getItem('token');
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        const response = await axios.get('sectors/');
        this.sectors = response.data.reduce((map, sector) => {
          map[sector.id] = sector.sector;
          return map;
        }, {});
      }
      //errors
      catch (error) {
        console.error('Error fetching clients:', error);
      }
    }
  }
};
</script>

<style scoped>
span {
  font-weight: normal;
  font-size: 1rem;
}
h5 {
  margin-left: 20px;
}
</style>