export interface ResponseModel<T> {
  status: number
  message: string
  response?: T
}
