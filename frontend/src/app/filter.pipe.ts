import { Pipe, PipeTransform } from '@angular/core';
import { Tree } from './trees/tree.model';

@Pipe({
  name: 'filter'
})
export class FilterPipe implements PipeTransform {
  transform(items: any[], searchText: string): any[] {

    if (!items) {
      return [];
    }
    if (!searchText) {
      return items;
    }
    searchText = searchText.toLocaleLowerCase();
    if (typeof(items[0].title) !== typeof(undefined)){
      const treeList: Tree[] = items;
      return treeList.filter(it => {
        return it.title.toLocaleLowerCase().includes(searchText);
      });
    }
    return items.filter(it => {
      return it.toLocaleLowerCase().includes(searchText);
    });
  }
}
