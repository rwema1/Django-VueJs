<template>
    <h2>CLIENTS</h2>
    <!-- List of Clients -->
    <div class="container">
      <div v-if="clients.length > 0">
        <ul class="list-group list-group-flush">
          <div class="list-group-item" v-for="client in clients" :key="client.id">
            <div class="po2 d-flex">
              <router-link :to="`/client/${client.id}/projects`" class="mr-auto p-2 align-items-center"><p>{{ client.name }}</p></router-link>
              <button @click="editClient(client)" class="btn btn-outline-secondary btn-sm p-2">Edit</button>
              <button @click="deleteClient(client.id)" class="btn btn-outline-secondary btn-sm p-2">Delete</button>
            </div>
          </div>
          <div class="list-group-item">
            <button @click="addClient()" class="btn btn-outline-secondary btn-sm">NEW CLIENT</button>
          </div>
        </ul>   
      </div>
    </div> 

    <!-- editing/updating clients -->
    <div v-if="isUpdating">
      <h2>Edit Client</h2>
      <div class="list-group list-group-flush">
        <form class="list-group-item" @submit.prevent="updateClient">
          <label class="form-group">Name:</label>
          <input type="text" class="form-control" v-model="updatedClient.name" required>
          <div class="d-flex">
            <button type="submit" class="btn btn-outline-secondary btn-sm p-2">Update</button>
            <button @click="closeEdit()" class="btn btn-outline-secondary btn-sm p-2">Close</button>
          </div>
        </form>
      </div>
    </div>
    
    <!-- Creating Clients -->
    <div v-if="isCreating">
      <h2>Add New Client</h2>
      <form class="list-group-item" @submit.prevent="createClient">
        <label class="form-group">Name:</label>
        <input type="text" class="form-control" v-model="newClient.name" required>
        <div class="d-flex">
          <button type="submit" class="btn btn-outline-secondary">Add Client</button>
          <button @click="closeEdit2()" class="btn btn-outline-secondary btn-sm p-2">Close</button>
        </div>
      </form>
    </div>

    <!-- Error Message -->
    <p v-if="error" style="color: red;">{{ error }}</p>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ClientsPage',

  data() {
    return {
      clients: [],
      newClient: { name: ''},
      updatedClient: { id: null, name: '' },
      isUpdating: false,
      isCreating: false,
      error: null
    };
  },
  created() {
    this.fetchClients();
  },
  methods: {
    //fetching clients
    async fetchClients() {
      try {
        //retrieving user token
        const token = localStorage.getItem('token');
        const response = await axios.get('clients/', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        //storing clients data
        this.clients = response.data;
        console.log('this.clients', this.clients);
      } catch (error) {
        console.error('Error fetching clients:', error);
        this.error = 'Failed to fetch clients. Please try again later.';
      }
    },

    //creating a new client
    async createClient() {
      //retrieving user token
      const token = localStorage.getItem('token');
      
      try {
          axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
          await axios.post('clients/', this.newClient);
          this.$router.go();
      }
      //errors
      catch (error) {
          console.error('Error creating client:', error);
          this.error = 'Failed to create client. Please try again.';
      }
    },
    addClient() {
      this.isCreating = true;
    },
    editClient(client) {
      this.isUpdating = true;
      this.updatedClient.id = client.id;
      this.updatedClient.name = client.name;
    },
    closeEdit() {
      this.isUpdating = false;
    },
    closeEdit2() {
      this.isCreating = false;
    },

    //editing/updating clients
    async updateClient() {
      try {
        const token = localStorage.getItem('token');
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        await axios.put(`clients/${this.updatedClient.id}/`, this.updatedClient);
        this.updatedClient = { id: null, name: '' };
        this.fetchClients();
      }
      catch (error) {
        console.error('Error updating client:', error);
        this.error = 'Failed to update client. Please try again.';
      }
    },

    //deleting client
    async deleteClient(clientId) {
      try {
        const token = localStorage.getItem('token');
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        await axios.delete(`clients/${clientId}/`);
        this.fetchClients();
      }
      catch (error) {
        console.error('Error deleting client:', error);
        this.error = 'Failed to delete client. Please try again.';
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
