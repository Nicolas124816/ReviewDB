import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MovieService {
  private apiUrl = 'http://127.0.0.1:8000/prompt/';

  constructor(private http: HttpClient) { }

  getMovieListFromDescription(description: string): Observable<any> {
    const requestData = { description };

    return this.http.post<any>(`${this.apiUrl}/getMovieListFromDescription`, requestData);
  }

  getMovieImageFromMovieName(movieName: string, movieYear: number): Observable<any> {
    const requestData = { movieName, movieYear };

    return this.http.post<any>(`${this.apiUrl}/getMovieImageFromMovieName`, requestData);
  }
}
