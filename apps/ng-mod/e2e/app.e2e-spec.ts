import { NgModPage } from './app.po';

describe('ng-mod App', function() {
  let page: NgModPage;

  beforeEach(() => {
    page = new NgModPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
