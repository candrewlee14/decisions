export class Tree {
    constructor(
      public title: string,
      public description: string,
      public isPrivate: boolean,
      public _id?: string,
      public updatedAt?: Date,
      public createdAt?: Date,
      public createdBy?: string,
    ) { }
  }
