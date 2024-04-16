<template>
  <div>
    <div>
      <h2>PROJECTS</h2>
      <!-- List of Projects -->
      <div v-if="projects.length > 0">
        <ul class="list-group list-group-flush">
          <div class="list-group-item" v-for="project in projects" :key="project.id">
            <div class="po2 d-flex">
            <p class="mr-auto p-2 align-items-center"><router-link :to="`/project/${project.id}`">{{ project.project_name }}</router-link></p>
            <p v-if="project.sector">{{ project.sector.sector }}</p>
          <button @click="editProject(project)" class="btn btn-outline-secondary btn-sm p-2"><a href="#edit">Edit</a></button>
            <button @click="deleteProject(project.id)" class="btn btn-outline-secondary btn-sm p-2">Delete</button>
            </div>
          </div>
          <div class="list-group-item">
            <router-link to="/new-project" taggert="_blank"><button class="btn btn-outline-secondary btn-sm">NEW PROJECT</button></router-link>
          </div>
        </ul>
      </div>
      <div v-else>
        <router-link to="/new-project" taggert="_blank"><button class="btn btn-outline-secondary btn-sm">NEW PROJECT</button></router-link>
      </div>
    </div>

    <div id='edit' v-if="isUpdating" class="app">
      <div class="auth-inner">
      <h1>Edit Project</h1>
      <!-- Update Project Form -->
      <form @submit.prevent="updateProject">
        <div>
        <label class="form-group">Project Name:</label>
        <input type="text" v-model="updatedProject.project_name" class="form-control" required>
        <label class="form-group">Details:</label>
        <textarea v-model="updatedProject.details" class="form-control" id="exampleFormControlTextarea1" required></textarea>
        <label class="form-group">Client:</label>
        <select v-model="updatedProject.client_name" class="form-control" required>
          <option v-for="client in clients" :key="client.id" :value="client.id">{{ client.name }}</option>
        </select>
        <label class="form-group">Sector:</label>
        <select v-model="updatedProject.sector" class="form-control" required>
          <option v-for="sector in sectors" :key="sector.id" :value="sector.id">{{ sector.sector }}</option>
        </select>
        </div>
        <button type="submit" class="btn btn-outline-secondary btn-sm">Update Project</button>
      </form>
      </div>
    </div>
    <!-- Error Message -->
    <p v-if="error" style="color: red;">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ProjectsPage',

  data() {
    return {
      projects: [],
      updatedProject: { id: null, project_name: '', details: '', client_name: '', sector: '' },
      clients: [],
      sectors: [],
      isUpdating: false,
      error: null
    };
  },
  
  async created() {
    await this.fetchProjects();
    await this.fetchClients();
    await this.fetchSectors();
  },
  
  methods: {
    async fetchProjects() {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('projects/', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        console.log('Projects:', response.data);
        this.projects = response.data;
      } catch (error) {
        console.error('Error fetching projects:', error);
        this.error = 'Failed to fetch projects. Please try again later.';
      }
    },
    
    async fetchClients() {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('clients/', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        this.clients = response.data;
      } catch (error) {
        console.error('Error fetching clients:', error);
        this.error = 'Failed to fetch clients. Please try again later.';
      }
    },
    
    async fetchSectors() {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('sectors/', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        this.sectors = response.data;
      } catch (error) {
        console.error('Error fetching sectors:', error);
        this.error = 'Failed to fetch sectors. Please try again later.';
      }
    },
    
    editProject(project) {
      console.log('Editing project:', project);
      if (project && project.id && project.client_name && project.sector) {
        this.isUpdating = true;
        this.updatedProject.id = project.id;
        this.updatedProject.project_name = project.project_name;
        this.updatedProject.details = project.details;
        this.updatedProject.client_name = project.client_name;
        this.updatedProject.sector = project.sector;
      } else {
        console.error('Invalid project object:', project);
      }
    },
    
    async updateProject() {
      try {
        const token = localStorage.getItem('token');
        await axios.put(`projects/${this.updatedProject.id}/`, this.updatedProject, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        this.isUpdating = false;
        this.updatedProject = { id: null, project_name: '', details: '', client_name: '', sector: '' };
        await this.fetchProjects();
      } catch (error) {
        console.error('Error updating project:', error);
        this.error = 'Failed to update project. Please try again.';
      }
    },
    
    async deleteProject(projectId) {
      try {
        const token = localStorage.getItem('token');
        await axios.delete(`projects/${projectId}/`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        await this.fetchProjects();
      } catch (error) {
        console.error('Error deleting project:', error);
        this.error = 'Failed to delete project. Please try again.';
      }
    }
  }
};
</script>

<style scoped>
.po2 {
  height: 38px;
}
.po2 button {
  margin-right: 8px;
}
router-link {
  color: inherit;
  text-decoration: none;
}

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
a {
  color: inherit;
  text-decoration: none;
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
  margin: 20px auto;
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
.auth-inner button {
  margin-top: 15px;
  display: flex;
  justify-content: center;
}
.auth-inner label {
  margin-top: 15px;
  margin-bottom: 2px;
}
.custom-control-label {
  font-weight: 400;
}
</style>