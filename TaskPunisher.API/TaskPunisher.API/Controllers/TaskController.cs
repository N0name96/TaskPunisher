using Microsoft.AspNetCore.Mvc;
using TaskPunisher.API.Models;
using TaskPunisher.API.Models.Interfaces;

namespace TaskPunisher.API.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class TaskController : Controller, ITaskController
    {
        private readonly ITaskService _taskService;

        public TaskController(ITaskService taskService)
        {
            _taskService = taskService ?? throw new ArgumentNullException(nameof(taskService));
        }

        /// <summary>
        /// Función que crea la nueva tarea
        /// </summary>
        /// <param name="task"></param>
        /// <returns>Response</returns>
        [HttpPost]
        [Route("/Create")]
        public async Task<Response> CreateTask(Task task)
        {
            Response response;

            try
            {
                int result = await _taskService.CreateTask(task);

                if (result == 0)
                {
                    throw new Exception("No se ha prodido crear la tarea correspondiente");
                }

                response = new Response
                {
                    status = StatusType.Succes,
                    message = "Se ha creado la tarea correctamente"
                };
            }
            catch (Exception ex)
            {
                response = new Response
                {
                    status = StatusType.Error,
                    message = $"Error a la hora de crear la tarea, {ex.Message}"
                };
            }

            return response;
        }

        [HttpDelete]
        [Route("/Delete")]
        public async Task<Response> DeleteTask(int id)
        {
            throw new NotImplementedException();
        }

        [HttpGet]
        [Route("/Get")]
        public async Task<Response> GetTask()
        {
            throw new NotImplementedException();
        }

        [HttpGet]
        [Route("/Get/{id}")]
        public async Task<Response> GetTaskId(int id)
        {
            throw new NotImplementedException();
        }

        [HttpPut]

        public async Task<Response> UpdateTask(Task task, int id)
        {
            throw new NotImplementedException();
        }
    }
}
