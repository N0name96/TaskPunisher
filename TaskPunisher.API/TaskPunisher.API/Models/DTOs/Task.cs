namespace TaskPunisher.API.Models.DTOs
{
    public class Task
    {
        public int Id { get; set; }
        public string Description { get; set; }
        public bool isCompleted { get; set; } = false;
    }
}
