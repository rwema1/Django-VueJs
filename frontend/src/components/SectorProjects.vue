<template>
  <div>
    <div v-if="projects && projects.length === 0">
      <p>No projects available.</p>
      <router-link to="/new-project" target="_blank">
        <button class="btn btn-outline-secondary">CREATE PROJECT</button>
      </router-link>
    </div>

    <!-- List of Projects -->
    <div v-else>
      <h1 v-if="projects && projects.length > 0">{{ getSector() }}<br></h1>
      <ul class="list-group list-group-flush">
        <div class="list-group-item" v-for="project in projects" :key="project.id">
          <h4>Project name: <span>{{ project.project_name }}</span></h4>
          <h5 v-if="project.client_name">client: <span>{{ getClientName(project.client_name) }}</span></h5>
          <br>
          <p>{{ project.details }}</p>
        </div>
      </ul>
    </div>

    <!-- Error Message -->
    <p v-if="error" style="color: red;">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SectorProjects',

  data() {
    return {
      projects: [],
      sectors: {},
      clients: {},
      error: null
    };
  },

  async created() {
    const sector_id = this.$route.params.id;

    await this.fetchProjects(sector_id);
    await this.fetchSectors();
    await this.fetchClients();
  },

  methods: {
    async fetchProjects(sector_id) {
      const token = localStorage.getItem('token');
      try {
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        const response = await axios.get(`sectors/${sector_id}/projects/`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        this.projects = response.data;
      } catch (error) {
        console.error('Error fetching projects:', error);
        this.error = 'Failed to fetch projects. Please try again later.';
      }
    },

    async fetchSectors() {
      try {
        const token = localStorage.getItem('token');
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        const response = await axios.get('sectors/');
        this.sectors = response.data.reduce((map, sector) => {
          map[sector.id] = sector.sector;
          return map;
        }, {});
      }
      catch (error) {
        console.error('Error fetching sectors:', error);
      }
    },
    async fetchClients() {
      try {
        const token = localStorage.getItem('token');
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        const response = await axios.get('clients/');
        this.clients = response.data.reduce((map, client) => {
          map[client.id] = client.name;
          return map;
        }, {});
      }
      catch (error) {
        console.error('Error fetching clients:', error);
      }
    },

    getSector() {
      const sector_id = this.$route.params.id;
      return this.sectors[sector_id];
    },

    getClientName(client_id) {
      return this.clients[client_id];
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