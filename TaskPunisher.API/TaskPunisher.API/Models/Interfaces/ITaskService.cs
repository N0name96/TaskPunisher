namespace TaskPunisher.API.Models.Interfaces
{
    public interface ITaskService
    {
        public Task<int> CreateTask(Task task);
        public Task<int> GetTask();
        public Task<int> GetTaskId(int id);
        public Task<int> UpdateTask(Task task, int id);
        public Task<int> DeleteTask(int id);
    }
}
