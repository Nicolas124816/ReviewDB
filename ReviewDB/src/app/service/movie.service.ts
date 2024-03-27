import { HttpClient, HttpHeaders, HttpRequest } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MovieService {
  private apiUrlBase = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) { }

  getMovieListFromDescription(prompt: string, kid: string, genre: string): Observable<any> {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Accept': 'text/plain'
    });
    const requestData = { prompt, kid, genre };
    let req = new HttpRequest<any>(
      'POST',
      this.apiUrlBase + `/prompt/test/`,
      requestData,
      {
        headers: headers,
        responseType: 'json'
      }
    );

    return this.http.request<any>(req);


    

    // return this.http.post<any>(`${this.apiUrlBase}/prompt/test/`, requestData, { headers });
  }
}
