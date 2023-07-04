<template>
  <div class="container">
    <itemForm
      :containerID=containerID
      v-if="showItemForm"
      @showItemForm="showItemForm = $event"
      @showContainerItems="showContainerItems = $event">
    </itemForm>
  </div>
  <div class="container" v-if="showContainerItems">
    <div class="row">
      <div class="col-sm-10">
        <h2>{{ name }}: Items</h2>
        <br>
        <alert :message=message v-if="showMessage"></alert>
        <button
          type="button"
          class="btn btn-success"
          @click="handleNewButton">
          New Item
        </button>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in items">
              <td>{{ item.name }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-primary btn-sm">View</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
import ItemForm from './ItemForm.vue';

export default {
  data() {
    return {
      name: '',
      items: [],
      containerID: null,
      showContainerItems: true,
      showItemForm: false,
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
    itemForm: ItemForm,
  },
  methods: {
    getItems() {
      const path = `http://localhost:5001/containers/${this.containerID}`;
      axios.get(path)
        .then((res) => {
          this.name = res.data.name;
          this.items = res.data.items;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    handleNewButton() {
      this.showItemForm = true;
      this.showContainerItems = false;
    },
    handleMessage(message) {
      this.showMessage = true;
      this.message = message;
      setTimeout(() => {
        this.showMessage = false;
      }, 5000);
    },
  },
  created() {
    this.containerID = this.$route.params.containerID;
    this.getItems();
  },
};
</script>
