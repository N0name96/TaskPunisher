namespace TaskPunisher.API.DTOs
{
    public class Punishment
    {
        public int Id { get; set; }
        public string Description { get; set; }
        public bool isCompleted { get; set; } = false;
    }
}
