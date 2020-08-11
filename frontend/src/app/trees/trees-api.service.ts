import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs'
import  {catchError} from 'rxjs/operators'
import {API_URL} from '../env';
import {Tree} from './tree.model';

@Injectable()
export class TreesApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  // GET list of public, future events
  getTrees(): Observable<Tree[]> {
    return this.http
      .get<Tree[]>(`${API_URL}/decisions`)
      .pipe(catchError(TreesApiService._handleError);
  }
}
