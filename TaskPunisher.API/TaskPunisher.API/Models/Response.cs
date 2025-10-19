namespace TaskPunisher.API.Models
{
    public class Response
    {
        public StatusType status {  get; set; }
        public string message { get; set; }
        
       public Response(StatusType status, string message)
       {
           this.status = status;
           this.message = message;
       }

        public Response() 
        {
            this.status = StatusType.Succes;
            this.message = "";
        }
    }
}
