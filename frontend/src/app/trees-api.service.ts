import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable, of, throwError} from 'rxjs';
import {catchError, map, tap} from 'rxjs/operators';
import {API_URL} from './env';
import {Tree} from './trees/tree.model';
import {Decision} from './decision.models';
import { MessageService } from './message.service';
import { _ParseAST } from '@angular/compiler';

@Injectable()
export class TreesApiService {

  private decisionsUrl = `${API_URL}/decisions/`;
  private decisionUrl = `${API_URL}/decision/`;

  constructor(
    private http: HttpClient,
    private messageService: MessageService) {
  }

  private static _handleError(err: HttpErrorResponse | any): Observable<never> {
    return err.pipe(throwError(err.message || 'Error: Unable to complete request.'));
  }

  /** GET list of decision trees from the server */
  getPublicTrees(): Observable<Tree[]> {
    return this.http
      .get<Tree[]>(this.decisionsUrl)
      .pipe(
      tap(_ => this.log(`fetched public trees`)),
      catchError(this.handleError<Tree[]>('getPublicTrees')));
  }

  /** GET tree by id. Will 404 if id not found */
  getDecision(id: string): Observable<Decision> {
    const url = `${this.decisionUrl}/${id}`;
    return this.http.get<Decision>(url).pipe(
      tap(_ => this.log(`fetched tree id=${id}`)),
      catchError(this.handleError<Decision>(`getDecision id=${id}`))
    );
  }

  /**
   * Handle Http operation that failed.
   * Let the app continue.
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   */
  private handleError<T>(operation = 'operation', result?: T){
    return (error: any): Observable<T> => {

      console.error(error); // log to console instead
      this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

   /** Log a HeroService message with the MessageService */
   private log(message: string) {
    this.messageService.add(`TreesApiService: ${message}`);
  }

}
