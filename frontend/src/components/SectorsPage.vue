<template>
  <div>
    <h2>SECTORS</h2>   
      <!-- List of Sectors -->
      <div v-if="sectors.length > 0">
        
        <ul class="list-group list-group-flush">
          <div class="list-group-item" v-for="sector in sectors" :key="sector.id">
            <div class="po1"></div>
            <div class="po2 d-flex">
              <router-link :to="`/sector/${sector.id}/projects`" class="mr-auto p-2"><p>{{ sector.sector }}</p></router-link>
              <button @click="editSector(sector)" class="btn btn-outline-secondary btn-sm p-2">Edit</button>
              <button @click="deleteSector(sector.id)" class="btn btn-outline-secondary btn-sm p-2">Delete</button>
            </div>
          </div>
          <div class="list-group-item">
          <button @click="addSector()" class="btn btn-outline-secondary btn-sm">NEW SECTOR</button>
          </div>
        </ul>
      </div>
      
    <div v-if="isUpdating" class="app">
      <h2>Edit Client</h2>
      <div class="list-group list-group-flush">
      <!-- Update Client Form -->
        <form class="list-group-item" @submit.prevent="updateSector">
          
          <label class="form-group">Name:</label>
          <input type="text" class="form-control" v-model="updatedSector.sector" required>
          <div class="d-flex">
          <button type="submit" class="btn btn-outline-secondary btn-sm p-2">Update</button>
          <button @click="closeEdit()" class="btn btn-outline-secondary btn-sm p-2">Close</button>
          </div>
        </form>
    </div>
    </div>

    <div v-if="isCreating">
      <h2>Add New Sector</h2>
      <form class="list-group-item" @submit.prevent="createSector">
        <label class="form-group">Name:</label>
        <input type="text" class="form-control" v-model="newSector.sector" required>
        <div class="d-flex">
        <button type="submit" class="btn btn-outline-secondary p-2">Add Sector</button>
        <button @click="closeEdit2()" class="btn btn-outline-secondary btn-sm p-2">Close</button>
        </div>
      </form>
  </div>

    <!-- Error Message -->
    <p v-if="error" style="color: red;">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SectorsPage',

  data() {
    return {
      sectors: [],
      newSector: { sector: '' },
      updatedSector: { id: null, sector: '' },
      isUpdating: false,
      isCreating: false,
      error: null
    };
  },
  created() {
    this.fetchSectors();
  },
  methods: {
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
    async createSector() {
        const token = localStorage.getItem('token');
        
        try {
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
            await axios.post('sectors/', this.newSector);
            this.$router.go()
        }   
        catch (error) {
            console.error('Error creating sector:', error);
            this.error = 'Failed to create sector. Please try again.';
        }
    },
    addSector() {
      this.isCreating = true;
    },
    closeEdit2() {
      this.isCreating = false;
    },
    editSector(sector) {
      this.isUpdating = true;
      this.updatedSector.id = sector.id;
      this.updatedSector.sector = sector.sector;
    },
    closeEdit() {
      this.isUpdating = false;
    },
    async updateSector() {
      try {
        const token = localStorage.getItem('token');
        await axios.put(`sectors/${this.updatedSector.id}/`, this.updatedSector, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        this.isUpdating = false;
        this.updatedSector = { id: null, sector: '' };
        this.fetchSectors();
      } catch (error) {
        console.error('Error updating sector:', error);
        this.error = 'Failed to update sector. Please try again.';
      }
    },
    async deleteSector(sectorId) {
      try {
        const token = localStorage.getItem('token');
        await axios.delete(`sectors/${sectorId}/`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        this.fetchSectors();
      } catch (error) {
        console.error('Error deleting sector:', error);
        this.error = 'Failed to delete sector. Please try again.';
      }
    }
  }
};
</script>

<style scoped>
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
  width: 80%;
  margin: auto;
  background: #ffffff;
  box-shadow: 0px 14px 80px rgba(34, 35,58, 0.1);
  padding: 40px 60px 45px 60px;
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
form button, h2 {
  margin-top: 15px;
  margin-right: 10px;
}
form h2 {
  margin-top: 10px;
}
form label {
  margin-top: 10px;
  margin-bottom: 2px;
}
form input {
  width: 350px;
}
</style>