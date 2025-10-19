namespace TaskPunisher.API.Models.Interfaces
{
    public interface ITaskController
    {
        public Task<Response> CreateTask (Task task);
        public Task<Response> GetTask();
        public Task<Response> GetTaskId(int id);
        public Task<Response> UpdateTask (Task task, int id);
        public Task<Response> DeleteTask (int id);
    }
}
