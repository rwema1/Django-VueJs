<template>
    <div>
        <ul class="list-group list-group-flush">
        <div class="list-group-item">
          <h1>{{ projects.project_name }}</h1>
          <h6 v-if="projects.sector && sectors[projects.sector]">Sector: <span>{{ sectors[projects.sector] }}</span></h6>
          <h6 v-if="projects.client_name && clients[projects.client_name]">Client: <span class='po'>{{ clients[projects.client_name] }}</span></h6>
        </div>
          <br>
          <p>{{ projects.details }}</p>
        </ul>
    </div>

    <!-- Error Message -->
    <p v-if="error" style="color: red;">{{ error }}</p>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ProjectName',

  data() {
    return {
      projects: [],
      sectors: {},
      clients: {},
      error: null
    };
  },
  

  async created() {
    const project_id = this.$route.params.id;

    await this.fetchProjects(project_id);
    await this.fetchSectors();
    await this.fetchClients();
  },

  methods: {
    async fetchProjects(project_id) {
      const token = localStorage.getItem('token');
      try {
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        const response = await axios.get(`projects/${project_id}/`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        console.log('Project:', response.data);
        this.projects = response.data
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
      } catch (error) {
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
      } catch (error) {
        console.error('Error fetching sectors:', error);
      }
    }
  }
};
</script>

<style scoped>
h1 span {
  font-weight: normal;
  font-size: 1.8rem;
}
h6 {
    margin-left: 20px;
}
h5 span {
  font-weight: normal;
  font-size: 1rem;
}
</style>