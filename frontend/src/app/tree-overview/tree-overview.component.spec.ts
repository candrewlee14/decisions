import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TreeOverviewComponent } from './tree-overview.component';

describe('TreeOverviewComponent', () => {
  let component: TreeOverviewComponent;
  let fixture: ComponentFixture<TreeOverviewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TreeOverviewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TreeOverviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
