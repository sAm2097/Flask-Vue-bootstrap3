<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>All Tasks</h1>
        <hr />
        <br /><br />
        <alert :message="message" v-if="showMessage"></alert>
        <button
          type="button"
          class="btn btn-success btn-sm"
          v-b-modal.task-modal
          >
          Add New Task
        </button>

        <br /><br />
        <main>

        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Description</th>
              <th scope="col">Folder</th>
              <!-- <th scope="col">X-Parameter</th>
              <th scope="col">Y-Parameter</th> -->
              <th scope="col">Task?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(task, index) in tasks" :key="index">
              <td>{{ task.title }}</td>
              <td>{{ task.description }}</td>
              <td>{{ task.folder }}</td>

              <!-- <td>{{ task.X }}</td>
              <td>{{ task.Y }}</td> -->
              <td>
                <span v-if="task.read">Completed</span>
                <span v-else>In process</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                    type="button"
                    class="btn btn-warning btn-sm"
                    v-b-modal.task-update-modal
                    @click="editTask(task)"
                    >Update</button
                  >
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="onDeleteTask(task)"
                    >Delete</button
                  >
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        </main>
      </div>
    </div>

    <!-- Here the new task will be added -->
    <b-modal
      ref="addTaskModal"
      id="task-modal"
      title="Add a new Task"
      hide-footer
    >
      <section v-if="showFolders">
        <div>
          <b-button variant="primary" @click="showFolders = !showFolders">Back</b-button>
        </div>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Folder name</th>
              <th scope="col">Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(folder, index) in folders" :key="index">
              <td>{{ folder }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                    type="button"
                    class="btn btn-warning btn-sm"
                    @click="openFolder(folder)"
                    >Open</button
                  >
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="selectFolder(folder)"
                    >Select</button
                  >
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </section>
      <section v-else>
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group
            id="form-title-group"
            label="Title:"
            label-for="form-title-input"
          >
            <b-form-input
              id="form-title-input"
              type="text"
              v-model="addTaskForm.title"
              required
              placeholder="Enter title"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group
            id="form-decription-group"
            label="Description:"
            label-for="form-description-input"
          >
            <b-form-input
              id="form-description-input"
              type="text"
              v-model="addTaskForm.description"
              required
              placeholder="Enter Description"
            >
            </b-form-input>
          </b-form-group>

            <!-- button to select folder of images to train -->
          <b-button variant="primary" @click="getFolders()">Select folder </b-button>
          <div class="my-2">
            Selected folder: {{ selectedFolder }}
          </div>

          <!-- For loop to run key values from json to train from selected folder of images -->

          <b-form-group v-for="(value,key) in Jsonfile"

          :key="value"

          :label="key"
          >
          <div v-if="typeof value === 'object'">
             <b-button v-b-toggle="'collapse'+key" class="m-1">{{key}}</b-button>

                <!-- Element to collapse -->
                <!-- key+key1,key+key1+'input' will generating a string -->
                  <b-collapse :id="'collapse'+key">
                    <b-card>
                      <b-form-group v-for="(value1,key1) in value"
                      :key="value1"


                      :label="key1"
                      >
                        <b-form-input

                          type="text"
                          v-model="formData[key][key1]"
                          required
                          placeholder="Enter value"

                        >
                        </b-form-input>
                      </b-form-group>
                    </b-card>
                  </b-collapse>

                   </div>
          <b-form-input v-else

              type="text"
              v-model="formData[key]"
              required
              placeholder="Enter value"

            >
            </b-form-input>

          </b-form-group>


   <!-- <b-form-group
            id="form-Xpara-group"
            label="X-Parameter:"
            label-for="form-Xpara-input"
          >
            <b-form-input
              id="form-Xpara-input"
              type="text"
              v-model.number="addTaskForm.X" number
              required
              placeholder="Enter X-Parameter"

            >
            </b-form-input>
          </b-form-group>

          <b-form-group
            id="form-Ypara-group"
            label="Y-Parameter:"
            label-for="form-Ypara-input"
          >
            <b-form-input
              id="form-Ypara-input"
              type="text"
              v-model.number="addTaskForm.Y" number
              required
              placeholder="Enter Y-Parameter"

            >
            </b-form-input>
          </b-form-group>  -->

          <b-form-group id="form-read-group">
            <b-form-checkbox-group v-model="addTaskForm.read" id="form-checks">
              <b-form-checkbox value="true">Task?</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <b-button type="submit" variant="primary">Train</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
      </section>
    </b-modal>
    <!-- Editing and updating the task -->
    <b-modal
      ref="editTaskModal"
      id="task-update-modal"
      title="Update"
      hide-footer
    >
    <section v-if="showFolders">
        <div>
          <b-button variant="primary" @click="showFolders = !showFolders">Back</b-button>
        </div>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Folder name</th>
              <th scope="col">Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(folder, index) in folders" :key="index">
              <td>{{ folder }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                    type="button"
                    class="btn btn-warning btn-sm"
                    @click="openFolder(folder)"
                    >Open</button
                  >
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="selectFolder(folder)"
                    >Select</button
                  >
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </section>
      <section v-else>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group
          id="form-title-edit-group"
          label="Title:"
          label-for="form-title-edit-input"
        >
          <b-form-input
            id="form-title-edit-input"
            type="text"
            v-model="editForm.title"
            required
            placeholder="Enter title"
          >
          </b-form-input>
        </b-form-group>

        <b-form-group
          id="form-description-edit-group"
          label="Description:"
          label-for="form-description-edit-input"
        >
          <b-form-input
            id="form-description-edit-input"
            type="text"
            v-model="editForm.description"
            required
            placeholder="Enter description"
          >
          </b-form-input>

           <b-button variant="primary" @click="getFolders()">Select folder </b-button>
          <div class="my-2">
            Selected folder: {{ selectedFolder }}
          </div>

        </b-form-group>

        <!-- <b-form-group
          id="form-Xpara-edit-group"
          label="X-Parameter:"
          label-for="form-Xpara-edit-input"
        >
          <b-form-input
            id="form-Xpara-edit-input"
            type="number"
            v-model.number="editForm.X" number
            required
            placeholder="Enter Xpara"
          >
          </b-form-input>
        </b-form-group>

        <b-form-group
          id="form-Ypara-edit-group"
          label="Y-Parameter:"
          label-for="form-Ypara-edit-input"
        >
          <b-form-input
            id="form-Ypara-edit-input"
            type="number"
            v-model.number="editForm.Y" number
            required
            placeholder="Enter Ypara"
          >
          </b-form-input>
        </b-form-group> -->

        <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.read" id="form-checks">
            <b-form-checkbox value="true">Task?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>

        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
      </section>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      tasks: [],
      Jsonfile:{},
      formData: {},
      editForm: {
        id: '',
        title: '',
        description: '',
        X: 0,
        Y: 0,
        read: [],
      },
      addTaskForm: {
        title: '',
        description: '',
        X: 0,
        Y:0,
        read: [],
      },
      message: '',
      showMessage: false,
      showFolders: false,
      folders: [],
      selectedFolder: "None",
      folderStack: [],
    };
  },
  components: {
    alert: Alert,
  },

  methods: {
    async getFolders(){
       if (!this.showFolders) {
         this.folderStack = [];
       }
       const baseParentFolder = './uploaded_files/'
       const path = `http://localhost:5000/tasks/uploaded_files?path=${baseParentFolder}${this.folderStack.join('/')}`;

       const response = await axios
        .get(path)
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      this.folders = response['data'].data;
      this.showFolders = true;
    },

    openFolder(folder) {
      this.folderStack.push(folder);
      this.getFolders();
    },

    selectFolder(folder) {
      this.folderStack.push(folder);
      this.selectedFolder = this.folderStack.join('/');
      this.showFolders = !this.showFolders;
    },

    getTasks() {
      const path = 'http://localhost:5000/tasks';
      axios
        .get(path)
        .then((res) => {
          this.tasks = res.data.tasks;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

    // editing or updating the form

    editTask(task) {
      this.editForm = task;
    },

    //adding the new task
    jsonParams(){
      const path=`http://localhost:5000/tasks/parameters`;
      axios
      .get(path)
      .then((res)=>
      {
        this.Jsonfile = res.data;
        this.formData = {...this.Jsonfile}
        console.log(res);
        })

      .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });

    },

    addTask(payload) {
      const path = 'http://localhost:5000/tasks';
      axios
        .post(path, payload)
        .then(() => {
          this.getTasks();
          this.message = 'Task added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getTasks();
        });
    },

    removeTask(taskID) {
      const path = `http://localhost:5000/tasks/${taskID}`;
      axios
        .delete(path)
        .then(() => {
          this.getTasks();
          this.message = 'Task removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTasks();
        });
    },

    onDeleteTask(task) {
      this.removeTask(task.id);
    },

    getImages(){

    },

    initForm() {
      this.addTaskForm.title = '';
      this.addTaskForm.description = '';
      this.addTaskForm.X = '';
      this.addTaskForm.Y = '';
      this.addTaskForm.read = [];

      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.description = '';
      this.editForm.X = '';
      this.editForm.Y = '';
      this.editForm.read = [];
    },

    // event for submiting the task
    onSubmit(evt) {
      evt.preventDefault();
     // this.$refs.addTaskModal.hide();
      let read = false;
      if (this.addTaskForm.read[0]) read = true;
      const payload = {
        title: this.addTaskForm.title,
        description: this.addTaskForm.description,
        folder: this.selectedFolder,
        X: this.addTaskForm.X,
        Y: this.addTaskForm.Y,
        read, // property shorthand
      };
      this.addTask(payload);
      this.initForm();
    },

    // event for submitting the edited task
    onSubmitUpdate(evt) {
      evt.preventDefault();
      //this.$refs.editTaskModal.hide();
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        title: this.editForm.title,
        description: this.editForm.description,
        X: this.editForm.X,
        Y: this.editForm.Y,
        read,
      };
      this.updateTask(payload, this.editForm.id);
    },
  // Wiring up AJAX request
    updateTask(payload, taskID) {
      const path = `http://localhost:5000/tasks/${taskID}`;
      axios
        .put(path, payload)
        .then(() => {
          this.getTasks();

          // Alerting user
          this.message = 'Task updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTasks();
        });
    },

    onReset(evt) {
      evt.preventDefault();
      //this.$refs.addTaskModal.hide();
      this.initForm();
    },

    onResetUpdate(evt) {
      evt.preventDefault();
      //this.$refs.editTaskModal.hide();
      this.initForm();
      this.getTasks();
    },
  },


  async created() {
    this.getTasks();
    this.jsonParams();
    console.log(this.Jsonfile)
  },
};
</script>


<style scoped>
main {
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 1rem;
  margin: 2rem auto;
  max-width: 80rem;
}
</style>

