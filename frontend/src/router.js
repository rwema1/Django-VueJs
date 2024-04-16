import { createRouter, createWebHistory } from 'vue-router';
import RegisterPage from './components/RegisterPage.vue';
import LoginPage from './components/LoginPage.vue';
import HomePage from './components/HomePage.vue';
import ClientsPage from './components/ClientsPage.vue';
import SectorsPage from './components/SectorsPage.vue';
import ProjectsPage from './components/ProjectsPage.vue';
import ClientProjects from './components/ClientProjects.vue';
import SectorProjects from './components/SectorProjects.vue';
import ProjectName from './components/ProjectName.vue';
import CreateProject from './components/CreateProject.vue';

const routes = [
  {
    path: '/register',
    name: 'Register',
    component: RegisterPage
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage
  },
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/clients',
    name: 'Clients',
    component: ClientsPage
  },
  {
    path: '/sectors',
    name: 'Sectors',
    component: SectorsPage
  },
  {
    path: '/projects',
    name: 'Projects',
    component: ProjectsPage
  },
  {
    path: '/new-project',
    name: 'CreateProject',
    component: CreateProject
  },
  {
    path: '/client/:id/projects',
    name: 'ClientProject',
    component: ClientProjects
  },
  {
    path: '/sector/:id/projects',
    name: 'SectorProjects',
    component: SectorProjects
  },
  {
    path: '/project/:id',
    name: 'ProjectName',
    component: ProjectName
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;